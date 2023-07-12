import random
import urllib
import folium
import pandas as pd
import numpy as np
import osrm
import polyline

osrm.RequestConfig.host = "router.project-osrm.org"


ColSets = ['#1B9E77', '#D95F02', '#7570B3', '#E7298A', '#66A61E', '#E6AB02', '#A6761D', '#666666']

def visualize(csv_file, color):
    Schedule = pd.read_csv(csv_file)
    Vehicles = np.sort(np.unique(Schedule['VID']))

    for vid in Vehicles:
        Focused = Schedule[Schedule['VID'] == vid]
        First = Focused.head(1)
        Last = Focused.tail(1)

        waypts = [[0, First["From_Lon"].values[0], First["From_Lat"].values[0]]]
        focus_list = Focused.index.to_list()

        for row in range(focus_list[0], focus_list[-1]):
            via = (row, Focused.loc[row, 'To_Lon'], Focused.loc[row, 'To_Lat'])
            waypts.append(via)

        # 데이터프레임 생성
        df = pd.DataFrame(waypts, columns=["com", "lon", "lat"])

        # 위도 경도 값 리스트 생성
        try:
            trips = osrm.trip(df[["lon", "lat"]].values.tolist(), overview="full")
            print(trips)
        # 400 에러 예외 처리
        except urllib.error.HTTPError as e:
            print(e.code)
            print(e.read())

        trip = trips['trips'][0]['geometry']
        route = polyline.decode(trip)

        # 경로 시작 지점 & 종료 지점 & 거리
        start_point = [trips['waypoints'][0]['location'][1], trips['waypoints'][0]['location'][0]]
        end_point = [trips['waypoints'][1]['location'][1], trips['waypoints'][1]['location'][0]]
        distance = trips['trips'][0]['distance']

        ps = Focused[Focused['Task_Type'] == "Pickup"]
        ds = Focused[Focused['Task_Type'] == "Delivery"]

        MapResult = folium.Map(location=[(start_point[0] + end_point[0]) / 2, (start_point[1] + end_point[1]) / 2],
                               zoom_start=13)

        folium.TileLayer(tiles="CartoDB positron").add_to(MapResult)
        folium.PolyLine(locations=route, color=color).add_to(MapResult)

        for index, row in ps.iterrows():
            # popup = f"{df['com'][index]}-{vid}"
            folium.CircleMarker(
                location=[row['To_Lat'], row['To_Lon']],
                color='red',
                stroke=True,
                radius=3,
                fill_opacity=0.8
            ).add_to(MapResult)
            print(row['To_Lat'], row['To_Lon'])

    MapResult.save("Map.html")


visualize('MILP.csv', random.choice(ColSets))
