var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        datasets: [{
                label: 'This Week',
                data: [112, 219, 323, 521, 212, 333],
                backgroundColor: 'transparent',
                borderColor: 'orange',
                borderWidth: 4
            },
            {
                label: 'Past Week',
                data: [231, 329, 121, 125, 122, 413],
                backgroundColor: 'transparent',
                borderColor: 'silver',
                borderWidth: 3
            },
        ],
    },
    options: {
        tooltips: {
            enabled: true,
        },

        scales: {
            y: {
                beginAtZero: true
            }
        },

        plugins: {
            title: {

                display: true,
                text: "",
                align: "start",

            },
            legend: {

                position: "top",
                align: "end",
                labels: {
                    usePointStyle: true,

                },
            }
        },


    }
});