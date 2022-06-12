import React from "react";


// chart 사용
import ReactApexChart from 'react-apexcharts'




class MyChart extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      series: [{
        name: "Desktops",
        data: [10, 41, 35, 51, 49]
      },
      {
        name: "집에보내줘",
        data: [1, 4, 15, 41, 69]
      }],

      options: {  
        chart: {
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: true
        },
        stroke: {
          curve: 'straight'
        },
        title: {
          text: '머신러닝 드랍할걸',
          align: 'center'
        },
        grid: {
          row: {
            colors: ['#f3f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.3
          },
        },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov','Dec'],
        }
      }
    }
  }
  render() {
    return (
      <ReactApexChart
        options={this.state.options}
        series={this.state.series}
        typs='line'
        width={500}
        height={300}
        />
    );
  }
}

export default MyChart;