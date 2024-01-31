// Environmental Data Chart
document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/environmental_data/')
        .then(response => response.json())
        .then(data => {
            // Update environmental chart using Chart.js
            // Example: Create a bar chart with fetched data

            const environmentalCtx = document.getElementById('environmentalChart').getContext('2d');
            
            if (data.length > 0) {  // Check if data is available
                const labels = data.map(entry => entry.industry_category);
                const totalVehiclesData = data.map(entry => entry.total_vehicles);

                new Chart(environmentalCtx, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Total Vehicles',
                            data: totalVehiclesData,
                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
                            borderColor: 'rgba(75, 192, 192, 1)',
                            borderWidth: 1
                        }],
                    },
                });
            } else {
                // Optionally show a message if no data is available
                console.log('No environmental data available.');
            }
        })
        .catch(error => {
            console.error('Error fetching environmental data:', error);
        });
});

// Similar fetch and chart update logic for social data
