import React from "react";


// chart 사용
import ReactApexChart from 'react-apexcharts'



class MyChart extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      series: [{
        name: "Desktops",
        data: [10, 41, 35, 51, 49, 62, 69, 91, 148, 45,87,90]
      },
      {
        name: "집에보내줘",
        data: [1, 4, 15, 41, 69, 32, 39, 31, 48,25,64,100]
      }],

      options: {  
        chart: {
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'straight'
        },
        title: {
          text: '머신러닝 드랍할걸',
          align: 'left'
        },
        grid: {
          row: {
            colors: ['#f3f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.5
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