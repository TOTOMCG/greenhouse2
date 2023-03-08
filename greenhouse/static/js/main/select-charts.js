/*
chart selector helper by Daniil 
*/


document.addEventListener('DOMContentLoaded', function(){
  var item = localStorage.getItem('select');
  var select = document.getElementById("select");
  select.value = item;
});
function submitForm(){
  var select = document.getElementById("select");
  var value = select.options[select.selectedIndex].value;
  localStorage.setItem('select', value);
  window.location.reload();
}


if (localStorage.getItem('select') != 'Температура') {
  document.getElementById('temperature').style.display = 'none'
}
var ctx = document.getElementById('temperature').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
      labels: [
          {% for i in time %}
              {{i}},
          {% endfor %}
      ],
      datasets: [{
          fill: false,
          data: [
              {% for i in temperature %}
                  {{i}},
              {% endfor %}
          ],
          backgroundColor: 'rgba(216, 27, 96, 0.6)',
          borderColor: 'rgba(216, 27, 96, 1)',
          borderWidth: 1
      }]
  },
  options: {
      legend: {
          display: false
      },
      title: {
          display: true,
          text: 'Температура',
          position: 'top',
          fontSize: 16,
          padding: 20
      },
      scales: {
          yAxes: [{
              ticks: {
                  min: 0,
                  max: 100
              }
          }]
      }
  }
});


if (localStorage.getItem('select') != 'Влажность воздуха') {
  document.getElementById('humidity_air').style.display = 'none'
}
var ctx = document.getElementById('humidity_air').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
      labels: [
          {% for i in time %}
              {{i}},
          {% endfor %}
      ],
      datasets: [{
          fill: false,
          data: [
              {% for i in humidity_air %}
                  {{i}},
              {% endfor %}
          ],
          backgroundColor: 'rgba(216, 27, 96, 0.6)',
          borderColor: 'rgba(216, 27, 96, 1)',
          borderWidth: 1
      }]
  },
  options: {
      legend: {
          display: false
      },
      title: {
          display: true,
          text: 'Влажность воздуха',
          position: 'top',
          fontSize: 16,
          padding: 20
      },
      scales: {
          yAxes: [{
              ticks: {
                  min: 0,
                  max: 100
              }
          }]
      }
  }
});

if (localStorage.getItem('select') != 'Влажность почвы') {
  document.getElementById('humidity_earth').style.display = 'none'
}
var ctx = document.getElementById('humidity_earth').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
      labels: [
          {% for i in time %}
              {{i}},
          {% endfor %}
      ],
      datasets: [{
          fill: false,
          data: [
              {% for i in humidity_earth %}
                  {{i}},
              {% endfor %}
          ],
          backgroundColor: 'rgba(216, 27, 96, 0.6)',
          borderColor: 'rgba(216, 27, 96, 1)',
          borderWidth: 1
      }]
  },
  options: {
      legend: {
          display: false
      },
      title: {
          display: true,
          text: 'Влажность почвы',
          position: 'top',
          fontSize: 16,
          padding: 20
      },
      scales: {
          yAxes: [{
              ticks: {
                  min: 0,
                  max: 100
              }
          }]
      }
  }
});

if (localStorage.getItem('select') != 'Состояние форточек') {
  document.getElementById('window_pane').style.display = 'none'
}
var ctx = document.getElementById('window_pane').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
      labels: [
          {% for i in time %}
              {{i}},
          {% endfor %}
      ],
      datasets: [{
          fill: false,
          data: [
              {% for i in window_pane %}
                  {{i}},
              {% endfor %}
          ],
          backgroundColor: 'rgba(216, 27, 96, 0.6)',
          borderColor: 'rgba(216, 27, 96, 1)',
          borderWidth: 1
      }]
  },
  options: {
      legend: {
          display: false
      },
      title: {
          display: true,
          text: 'Состояние форточек',
          position: 'top',
          fontSize: 16,
          padding: 20
      },
      scales: {
          yAxes: [{
              ticks: {
                  min: 0,
                  max: 1
              }
          }]
      }
  }
});

if (localStorage.getItem('select') != 'Состояние полива') {
  document.getElementById('watering').style.display = 'none'
}
var ctx = document.getElementById('watering').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
      labels: [
          {% for i in time %}
              {{i}},
          {% endfor %}
      ],
      datasets: [{
          fill: false,
          data: [
              {% for i in watering %}
                  {{i}},
              {% endfor %}
          ],
          backgroundColor: 'rgba(216, 27, 96, 0.6)',
          borderColor: 'rgba(216, 27, 96, 1)',
          borderWidth: 1
      }]
  },
  options: {
      legend: {
          display: false
      },
      title: {
          display: true,
          text: 'Состояние полива',
          position: 'top',
          fontSize: 16,
          padding: 20
      },
      scales: {
          yAxes: [{
              ticks: {
                  min: 0,
                  max: 1
              }
          }]
      }
  }
});