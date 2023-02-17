var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['', '', ''],
        datasets: [{
            fill: false,
            data: [1, 0, 1, 0, 1, 0],
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
            text: 'Test',
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