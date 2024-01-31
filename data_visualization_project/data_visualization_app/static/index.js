// Environmental Data Chart
var environmentalData = {
    labels: [ `{% for data in environmental_data %}"{{ data.industry_category }}",{% endfor %} `],
    datasets: [{
        label: 'Total Vehicles',
        data: [ `{% for data in environmental_data %}{{ data.total_vehicles }},{% endfor %} `],
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
    }]
};

var environmentalCtx = document.getElementById('environmentalChart').getContext('2d');
var environmentalChart = new Chart(environmentalCtx, {
    type: 'bar',
    data: environmentalData
});

// Social Data Chart
var socialData = {
    labels: ['Total Employees', 'Female Employees', 'Male Employees'],
    datasets: [{
        data: [ `{% for data in social_data %}{{ data.total_employees }},{% endfor %} `],
        backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)'],
        borderColor: ['rgba(255,99,132,1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)'],
        borderWidth: 1
    }]
};

var socialCtx = document.getElementById('socialChart').getContext('2d');
var socialChart = new Chart(socialCtx, {
    type: 'pie',
    data: socialData
});
