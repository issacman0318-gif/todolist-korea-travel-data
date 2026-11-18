# Seoul Hotel Area Comparison｜首爾住宿區與車站

從仁川行李動線、首爾市區活動及隔日長途車三個情境比較住宿區。

## 用法

在下面比較交通方式與出發前查核事項。也可下載 [CSV](data.csv) 或 [JSON](data.json)，依城市或下一程用途篩選。考慮輪椅、嬰兒車或大型行李時，先以營運方的電梯及無障礙路徑公告確認完整動線。

弘大入口可搭 AREX 站站停。首爾站另有 AREX 直達車。明洞及東大門一帶宜按酒店地址選地鐵站和出口。

| 城市 | 站區 | 可核實銜接 | 適合先比較的情境 | 訂房前核對 | 來源 |
|---|---|---|---|---|---|
| 首爾 | 首爾站 | AREX 直達車與站站停 | 機場及長途鐵路銜接 | 分別查機場鐵路及長途鐵路的入口。 | [來源](https://english.visitseoul.net/airport-to-seoul) |
| 首爾 | 弘大入口 | AREX 站站停 | 機場直達站區與弘大行程 | 找到住宿靠哪側出口，再核對行李動線。 | [來源](https://english.visitseoul.net/airport-to-seoul) |
| 首爾 | 孔德 | AREX 站站停 | 機場與市區轉乘 | 入住前確認最近入口，並查市區目的地所需路線。 | [來源](https://english.visitseoul.net/airport-to-seoul) |
| 首爾 | 明洞站 | 首爾地鐵 4 號線 | 明洞步行區與市區行程 | 以酒店地址比對出口，機場鐵路方案另查首爾站轉乘。 | [來源](https://english.seoul.go.kr/wp-content/uploads/2026/03/2026_touristmap_EN.pdf) |
| 首爾 | 東大門歷史文化公園站 | 首爾地鐵 2／4／5 號線 | DDP 周邊住宿 | 和東大門站分開查，避免用相似站名估計步行距離。 | [來源](https://english.seoul.go.kr/wp-content/uploads/2026/03/2026_touristmap_EN.pdf) |

## 資料字典

- `city`、`area_or_station` 為城市及比較單位，兩欄合併辨識一筆。
- `verified_connection` 為來源可核實的運輸連接或規劃參照。
- `planning_use_case` 及 `check_before_booking` 為 Todolist 編輯整理的選區情境與核對事項。
- `source_url` 與 `checked_on` 為該列的第一手來源及核對日期。

## 方法、限制與授權

逐列查營運機構或政府原始資料，整理基本站名及服務事實，另加原創的住宿選區判斷。涵蓋選定站區。班表、營運異動、無障礙狀態、酒店距離、價格與評價請向各營運方及酒店核對。原創文字及欄位設計依 [專案授權](../LICENSE.md) 提供，原始資料頁、地圖和商標各依權利人條款。

資料核對日期 2026-11-19。

## 延伸住宿攻略

- [首爾站住宿](https://todolist-korea.com/seoul-station-hotels/)
- [弘大住宿](https://todolist-korea.com/hongdae-hotels/)
- [明洞住宿](https://todolist-korea.com/myeongdong-hotels/)
