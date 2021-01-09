html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.min.js" integrity="sha512-d9xgZrVZpmmQlfonhQUvTR7lMPtO7NkZMkA0ABN3PHCbKA5nqylQ/yWlFAyY6hYgdF1Qh6nYiuADWwKB4C2WSw==" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <script>
    var labels, backgroundColor, data, label, ctx, myChart;
    </script>
</head>
<body>
    {% for items in list_of_csv %}
        <div class="m-2 p-3">
            <div class="row">
                <div class="col-xl-4 col-lg-4">
                    <table class="table table-striped table-bordered">
                        <thead class="thead-dark">
                            {% for item in items[0] %}
                                <th>{{ item }}</th>
                            {% endfor %}
                        </thead>
                        <tbody class="table-striped">
                            {% for row in items[1] %}
                                <tr>
                                {% for item in row %}
                                    <td>{{ item }}</td>
                                {% endfor %}
                                </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
                <div class="col-xl-3 col-lg-3">
                    <canvas id="myChart-{{ loop.index }}" width="0" height="0"></canvas>
                    <img alt="Chart" id="myChart-{{ loop.index }}-img">
                </div>
            </div>
        </div>
        <script>
            labels = {{ label }};
            backgroundColor = [
                                    "#5ac18e","#40e0d0","#8b0000","#ff4040","#333333","#444d56",
                                    "#e6e6ea","#fed766","#f4b6c2","#6497b1","#4b86b4","#fe9c8f",
                                    "#e5edf1","#87cefa","#aec9eb","#efc5b5","#e1d590","#d3b683",
                                    "#e5ccbd","#d2bfc4","#ccfd7f","#b7d24b","#befd73","#64bfa4",
                                    "#bf77f6"];
            data = {{ value }};
            label = "Label of Pie Chart"
            ctx = document.getElementById("myChart-{{ loop.index }}").getContext("2d");
            myChart = new Chart(ctx, {
                type: "pie",
                data: {
                    labels: labels,
                    datasets: [{
                        label: label,
                        data: data,
                        backgroundColor: backgroundColor,
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    },
                    animation: {
                        onComplete: function() {
                            // console.log(myChart.toBase64Image());
                            document.getElementById('myChart-{{ loop.index }}-img').src = myChart.toBase64Image();
                            document.getElementById('myChart-{{ loop.index }}').style.display = "None";
                        }
                    }
                }
            });
        </script>
    {% endfor %}
</body>
</html>'''