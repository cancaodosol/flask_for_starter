# JR西日本の公開情報を取得する。

参考：https://gist.github.com/tomo0611/79db49172649bd4687a1683dd8ee3639

## 路線一覧

```http
GET https://www.train-guide.westjr.co.jp/api/v3/area_kinki_master.json
Content-Type: application/json
Accept: application/json
```

## JR京都線 （駅情報）

```http
GET https://www.train-guide.westjr.co.jp/api/v3/kyoto_st.json
Content-Type: application/json
Accept: application/json
```


## JR京都線 （車両位置情報）

```http
GET https://www.train-guide.westjr.co.jp/api/v3/kyoto.json
Content-Type: application/json
Accept: application/json
```

## 車両状況詳細

```http
GET https://www.train-guide.westjr.co.jp/api/v3/trainmonitorinfo.json
Content-Type: application/json
Accept: application/json
```


## 大阪メトロ　（車両位置取得）

```http
GET https://api.mobility-operation-info.emetro-app.osakametro.co.jp/app/api/v1/trainlocation?route_code=1
Content-Type: application/json
Accept: application/json
X-Api-Key: XSGUG4p5Ya5vQCehV3zZjaDheZAQMpqP9paVan8W
```

## 大阪メトロ　（駅の座標情報）
```http
GET https://static.mobility-operation-info.emetro-app.osakametro.co.jp/emetro/cache/common/json/stationCoords.json
Content-Type: application/json
Accept: application/json
X-Api-Key: XSGUG4p5Ya5vQCehV3zZjaDheZAQMpqP9paVan8W
```