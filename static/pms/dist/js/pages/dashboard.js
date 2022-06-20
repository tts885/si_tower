/*
 * Author: Abdullah A Almsaeed
 * Date: 4 Jan 2014
 * Description:
 *      This is a demo file used only for the main dashboard (index.html)
 **/

/* global moment:false, Chart:false, Sparkline:false */

$(function () {
  'use strict'

  // Make the dashboard widgets sortable Using jquery UI
  $('.connectedSortable').sortable({
    placeholder: 'sort-highlight',
    connectWith: '.connectedSortable',
    handle: '.card-header, .nav-tabs',
    forcePlaceholderSize: true,
    zIndex: 999999
  })
  $('.connectedSortable .card-header').css('cursor', 'move')

  // jQuery UI sortable for the todo list
  $('.todo-list').sortable({
    placeholder: 'sort-highlight',
    handle: '.handle',
    forcePlaceholderSize: true,
    zIndex: 999999
  })

})

/// ===グラフ描画Start=== ///
var endpoint = '/api/chart';

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    drawLineGraph(data, 'lineChart');
    drawBarGraph(data, 'barChart');
    drawWidget(data);
    console.log("drawing");
  },
  error: function (error_data) {
    console.log(error_data);
  }
})
var now = new Date();
function drawLineGraph(data, id) {
  var calendar = data.labels.calendar;
  var planCount = data.labels.planCount;
  var actualCount = data.labels.actualCount;
  var chartLabel = "予定";


  var Year = now.getFullYear();
  var Month = ('00' + (now.getMonth() + 1)).slice(-2);
  var Day = ('00' + now.getDate()).slice(-2);
  date = Year + "-" + Month + "-" + Day

  //  var count_plan = data.sumplan;
  //  var count_actual = data.sumactual;
  var ctx = document.getElementById(id).getContext('2d');
  var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
      labels: calendar,
      datasets: [{
        label: chartLabel,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgb(55, 99, 132)',
        data: planCount,
      }, {
        label: "実績",
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 206, 86, 0.2)',
        data: actualCount,
      }]
    },

    // Configuration options go here
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true
        },
        xAxes: [{
          display: true
        }],
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      },

      annotation: {
        annotations: [
          {
            type: "line",
            mode: "vertical",
            // scaleID: "x-axis-0",
            scaleID: "x-axis-0",
            value: date,
            borderColor: "red",
            borderWidth: 2,

            label: {
              content: "本日" + "(" + date + ")",
              enabled: true,
              position: "top"
            }
          }
        ]
      }
    }

  });
}

function drawBarGraph(data, id) {

  var labels = data.status.name;
  var chartLabel = "";
  var chartdata = data.status.count;

  var ctx = document.getElementById(id).getContext('2d');

  var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: labels,
      datasets: [{
        label: chartLabel,
        data: chartdata,
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      title: {
        display: true,
        text: "Status単位発生割合％"
      },
      legend: {
        position: "top"
      },
      responsive: true,
      maintainAspectRatio: false,
    },
    plugins: [PercentagePlugin],

  });
}

function drawWidget(data) {
  var total_work = document.getElementById('total_work');
  total_work.innerText = data.total_work
}

/// ===グラフ描画End=== ///