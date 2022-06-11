$(function () {

/** ****** add active class and stay opened when selected Start ***** */
var url = window.location;
const allLinks = document.querySelectorAll('.nav-item a');
const currentLink = [...allLinks].filter(e => {
return e.href == url;
});

if (currentLink.length > 0) { //this filter because some links are not from menu
  currentLink[0].classList.add("active");
  currentLink[0].closest(".nav-treeview").style.display = "block";
  //currentLink[0].closest(".has-treeview").classList.add("active");
}
/** ****** add active class and stay opened when selected End ***** */

/** ****** Initialize Select2 Elements Start ***** */
  $('.select2').select2()

  //Initialize Select2 Elements
  $('.select2bs4').select2({
    theme: 'bootstrap4'
  })
/** ****** Initialize Select2 Elements End ***** */

/** ****** Initialize Date picker Elements Start ***** */
  $.datetimepicker.setLocale('ja'); // 日本語化
  $('#planStartDate').datetimepicker({
    timepicker:false, // 日付のみ表示
    format:'Y-m-d', // フォーマットの指定。オプションはカンマ区切りで複数指定可能
  });
  $('#planEndDate').datetimepicker({
    timepicker:false, // 日付のみ表示
    format:'Y-m-d', // フォーマットの指定。オプションはカンマ区切りで複数指定可能
  });
  $('#actualStartDate').datetimepicker({
    timepicker:false, // 日付のみ表示
    format:'Y-m-d', // フォーマットの指定。オプションはカンマ区切りで複数指定可能
  });
  $('#actualEndDate').datetimepicker({
    timepicker:false, // 日付のみ表示
    format:'Y-m-d', // フォーマットの指定。オプションはカンマ区切りで複数指定可能
  });
  $('#createDate').datetimepicker({
    timepicker:false, // 日付のみ表示
    format:'Y-m-d', // フォーマットの指定。オプションはカンマ区切りで複数指定可能
  });
  $('#dueDate').datetimepicker({
    timepicker:false, // 日付のみ表示
    format:'Y-m-d', // フォーマットの指定。オプションはカンマ区切りで複数指定可能
  });

/** ****** Initialize Date picker Elements End ***** */

/** ****** Initialize easyMDE Start ***** */
  const easyMDE01 = new EasyMDE({element: document.getElementById('text-area1')});
  const easyMDE02 = new EasyMDE({element: document.getElementById('text-area2')});
  const easyMDE03 = new EasyMDE({element: document.getElementById('text-area3')});
  const easyMDE04 = new EasyMDE({element: document.getElementById('text-area4')});
/** ****** Initialize easyMDE Start ***** */

/** ****** Initialize DataTable Start ***** */
    $("#serach_workdata").DataTable({
      "responsive": true, "lengthChange": false, "autoWidth": false,
      //"buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"],
      "buttons": ["copy","excel","print", "colvis"],
      language: {
        "decimal": ".",
        "emptyTable":     "表示するデータがありません。",
        "thousands": ",",
        "sProcessing": "処理中...",
        "sLengthMenu": "_MENU_ 件表示",
        "sZeroRecords": "データはありません。",
        "sInfo": " _TOTAL_ 件中 _START_ から _END_ まで表示",
        "sInfoEmpty": " 0 件中 0 から 0 まで表示",
        "sInfoFiltered": "（全 _MAX_ 件より抽出）",
        "sInfoPostFix": "",
        "sSearch": "検索:",
        "sUrl": "",
        "oPaginate": {
          "sFirst": "先頭",
          "sPrevious": "前",
          "sNext": "次",
          "sLast": "最終"
        }
    },
    }).buttons().container().appendTo('#serach_workdata_wrapper .col-md-6:eq(0)');

    $("#get_historydata").DataTable({
      "responsive": true, "lengthChange": false, "autoWidth": false,
      //"buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"],
      "buttons": ["copy","excel","print", "colvis"],
      language: {
        "decimal": ".",
        "emptyTable":     "表示するデータがありません。",
        "thousands": ",",
        "sProcessing": "処理中...",
        "sLengthMenu": "_MENU_ 件表示",
        "sZeroRecords": "データはありません。",
        "sInfo": " _TOTAL_ 件中 _START_ から _END_ まで表示",
        "sInfoEmpty": " 0 件中 0 から 0 まで表示",
        "sInfoFiltered": "（全 _MAX_ 件より抽出）",
        "sInfoPostFix": "",
        "sSearch": "検索:",
        "sUrl": "",
        "oPaginate": {
          "sFirst": "先頭",
          "sPrevious": "前",
          "sNext": "次",
          "sLast": "最終"
        }
    },
    }).buttons().container().appendTo('#serach_workdata_wrapper .col-md-6:eq(0)');

  
    $("#res_data").DataTable({
      //"dom": 'Bfrtip',
      "responsive": true,
      "lengthChange": false,
      "autoWidth": false,
      "buttons": ["copy", "excel", "print", "colvis"],
      language: {
        "decimal": ".",
        "emptyTable":     "表示するデータがありません。",
        "thousands": ",",
        "sProcessing": "処理中...",
        "sLengthMenu": "_MENU_ 件表示",
        "sZeroRecords": "データはありません。",
        "sInfo": " _TOTAL_ 件中 _START_ から _END_ まで表示",
        "sInfoEmpty": " 0 件中 0 から 0 まで表示",
        "sInfoFiltered": "（全 _MAX_ 件より抽出）",
        "sInfoPostFix": "",
        "sSearch": "検索:",
        "sUrl": "",
        "oPaginate": {
              "sFirst": "先頭",
              "sPrevious": "前",
              "sNext": "次",
              "sLast": "最終"
            },
        },
      "ajax": {
           "url": "/lode_issue_data",
           "data": function( d ) {
                d.param1 = $('#data_pk').val();
            },
            "type": 'GET',
            "contentType": 'charset=utf-8',
            "dataSrc":'',
        },
      "columns": [
          {"data": 'pk'},
          { "data": 'fields.name' },
          { "data": 'fields.owner' },
        { "data": 'status_id'},
//        { "data": 'fields.name' },
      ],
    }).buttons().container().appendTo('#res_data_wrapper .col-md-6:eq(0)');
/** ****** Initialize DataTable End ***** */

})


/** ****** csrf_tokenの取得に使う ***** */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getModelInfo(url,search_id) {
    console.log('処理Start：')
    // setup for ajax
    var csrf_token = getCookie("csrftoken");
    var dataId = "data_id";
    var dataName = "data_name";

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });

    //let url = "/pms/work/getIssue/";
    $.ajax({
        //cache: false,
        url: url,
        type: "POST",
        data: {
        'search_id':$(search_id).val()
        },
        dataType: 'json'

    }).done(function(data) {
            // 通信成功時の処理を記述
            //setData(data)
            if (data != null){
                console.log('POST処理成功：' + data.search_id + 'name:' + data.name)
                document.getElementById(dataId).innerText = data.search_id
                document.getElementById(dataName).innerText = data.name
                document.getElementById(dataName).style.color = '#007bff';
                document.getElementById(dataId).style.color = '#007bff';
                document.getElementById("addRelation").disabled = false;
                setALink(dataId,data.search_id)
                setALink(dataName,data.search_id)

            }else{
                document.getElementById(dataId).innerText = 'E9999'
                document.getElementById(dataName).innerText = '該当IDに一致するデータが見つかりませんでした。';
                document.getElementById(dataName).style.color = '#ff0000';
                document.getElementById(dataId).style.color = '#ff0000';
                document.getElementById("addRelation").disabled = true;
            }
            //location.reload();

        })
        .fail(function() {
            // 通信失敗時の処理を記述
            $('#resultGET').text('GET処理失敗.');
            console.log('POST処理失敗')
        });
}

function setALink(linkID,index) {
    var linkURL = "/pms/issue/update/"+ index ;
    var baseTag = document.getElementById(linkID);
    var link1 = baseTag.firstChild.nodeValue;
    var aTag = document.createElement("a");
    aTag.href = linkURL;
    aTag.appendChild(document.createTextNode(link1));
    baseTag.replaceChild(aTag, baseTag.firstChild);
}

function add_Relation(url,search_id,index) {
    console.log('処理Start：')
    // setup for ajax
    var csrf_token = getCookie("csrftoken");
    const tab = document.getElementById('work');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });

    //let url = "/pms/work/addRelation/";
    $.ajax({
        //cache: false,
        url: url,
        type: "POST",
        data: {
        'search_id':$(search_id).val(),
        'index': index
        },
        dataType: 'json'

    }).done(function(data) {
            // 通信成功時の処理を記述
            location.reload()
        })
        .fail(function() {
            // 通信失敗時の処理を記述
            $('#resultGET').text('GET処理失敗.');
            console.log('POST処理失敗')
        });
}

//Modal画面DATA引き渡し
$(function() {
  $('.btn-outline-danger').on('click', function () {
  //alert($(this).data("url"))
     $("#parent_id").text($(this).data("parent_id"));
     $("#child_id").text($(this).data("child_id"));
     $('#del_url').attr('href', $(this).data("url"));
  });
});

//Tab Control(TABの状態を保持)
$(document).ready(function(){
    $('a[data-toggle="pill"]').on('show.bs.tab', function(e) {
        localStorage.setItem('activeTab', $(e.target).attr('href'));
    });
    var activeTab = localStorage.getItem('activeTab');
    if(activeTab){
        $('#custom-content-above-tab a[href="' + activeTab + '"]').tab('show');
    }
});