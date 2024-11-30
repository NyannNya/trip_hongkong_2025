# Itinerary Planner

這是一個基於 Streamlit 的旅遊行程規劃應用程式，使用者可以通過直觀的網頁介面查看每日的詳細行程。

## 目錄結構

```
app
├── components
│   ├── image_display.py
│   ├── itinerary_display.py
│   └── sidebar.py
├── data
│   ├── flight_data.py
│   └── itinerary_data.py
├── Dockerfile
├── image
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

## 功能概述
- **行程展示**: 每日行程顯示，方便使用者快速了解旅行計劃。
- **側邊欄選擇**: 使用者可在側邊欄中選擇不同日期來查看對應的行程。

## 專案文件說明

### `main.py`
這是專案的主文件，負責設定頁面配置，並控制側邊欄和行程展示的顯示。

- `display_sidebar()` 來自 `components/sidebar.py`，用於顯示側邊欄，並讓使用者選擇行程日期。
- `display_itinerary()` 來自 `components/itinerary_display.py`，負責顯示選定日期的詳細行程。
- `itinerary` 是一個字典，包含每一天的行程數據，來源於 `data/itinerary_data.py`。

### `components`
- **`sidebar.py`**: 負責側邊欄的顯示和互動邏輯。
- **`itinerary_display.py`**: 顯示每日行程詳細信息。
- **``image_display.py`**: 提供一些工具函數及顯示圖像的功能。

### `data`
- **`itinerary_data.py`**: 包含行程的數據，例如每一天的行程細節。
- **`flight_data.py`**: 如果需要，則用於管理飛行計劃的相關數據。

### `requirements.txt`
列出了專案所需的所有 Python 套件，例如 `streamlit`，確保所有依賴項都可以被順利安裝。

### `Dockerfile`
該文件用於創建應用的 Docker 容器，使專案能在不同環境中便捷地運行。

## 安裝與使用

### 先決條件
- Python 3.9

### 安裝步驟
1. clone
   ```
   git clone my-git-name.git
   cd your-file
   ```
2. insatll
   ```
   pip install -r requirements.txt
   ```
3. run：
   ```
   streamlit run main.py
   ```
4. 若使用 Docker：
   ```
   docker build -t your-app .
   docker run -p 8501:8501 your-app
   ```

## 使用方式
1. 開啟應用後，在頁面的左側可以看到日期的選擇欄。
2. 選擇日期後，右側的主要區域會顯示該日的詳細行程。

## 版權與授權
本專案遵循 MIT 許可證，詳細請參閱 [LICENSE](./LICENSE) 文件。
