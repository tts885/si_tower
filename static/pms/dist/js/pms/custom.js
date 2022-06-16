console.log("custom.js!!");
window.onload = (e) => {
console.log("onload!!");

  // キャンバスの取得
  const ctx = document.getElementById("my-chart").getContext("2d");
  // チャートオブジェクト
  const myChart = new Chart(ctx, {
    type: "line",// グラフの種類 ("bar" "line" "pie" "doughnut" "radar" "polarArea")
    data: {
      labels: ["Switch", "3DS", "DS", "SFC", "GB", "FC", "CC"],// ラベル
      datasets: [{
        label: "任天堂ハード販売台数1",// タイトル
        data: [2254, 2458, 3286, 1717, 3247, 1935, 2400],// データ
        backgroundColor: [
          "rgba(255, 100, 100, 0.2)",// 背景の色
          "rgba(100, 255, 100, 0.2)",
          "rgba(100, 100, 255, 0.2)",
          "rgba(255, 255, 100, 0.2)",
          "rgba(100, 255, 255, 0.2)",
          "rgba(255, 100, 255, 0.2)"
        ],
        borderColor: [
          "rgba(255, 100, 100, 1)",// 枠線の色
          "rgba(100, 255, 100, 1)",
          "rgba(100, 100, 255, 1)",
          "rgba(255, 255, 100, 1)",
          "rgba(100, 255, 255, 1)",
          "rgba(255, 100, 255, 1)"
        ],
        borderWidth: 1// 枠線の太さ
      },

      {
        label: "任天堂ハード販売台数2",// タイトル
        data: [3254, 3458, 3586, 2717, 3047, 2135, 2700],// データ
        backgroundColor: [
          "rgba(255, 100, 100, 0.2)",// 背景の色
          "rgba(100, 255, 100, 0.2)",
          "rgba(100, 100, 255, 0.2)",
          "rgba(255, 255, 100, 0.2)",
          "rgba(100, 255, 255, 0.2)",
          "rgba(255, 100, 255, 0.2)"
        ],
        borderColor: [
          "rgba(255, 100, 100, 1)",// 枠線の色
          "rgba(100, 255, 100, 1)",
          "rgba(100, 100, 255, 1)",
          "rgba(255, 255, 100, 1)",
          "rgba(100, 255, 255, 1)",
          "rgba(255, 100, 255, 1)"
        ],
        borderWidth: 1// 枠線の太さ
      }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}