import React from "react";


// chart 사용
import ReactApexChart from 'react-apexcharts'





// const keys = modelData.keys('chart_data'); 

class MyChart extends React.Component {
  constructor(props) {
    super(props);
// [2주(일)전 판매량, 1주 전 판매량, 오늘 판매량, 예측값]
    this.state = {
      series: [{
        name: "1번아이템",
        data: [3, 5, 10, 3]
      },
      {
        name: "2번아이템",
        data: [3, 5, 2, 10]
      },
      {
        name: "3번아이템",
        data: [5, 6, 6, 12]
      },
      {
        name: "4번아이템",
        data: [1, 5, 3, 10]
      },
      {
        name: "5번아이템",
        data: [1, 4, 15, 8]
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
          text: '판매량 추이',
          align: 'center'
        },
        grid: {
          row: {
            colors: ['#f3f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.3
          },
        },
        xaxis: {
          categories: ['저저번주', '저번주', '이번주', '다음주(예측)'],
        }
      }
    }
  }
  render() {
    return (
    <div>
      <ReactApexChart
        options={this.state.options}
        series={this.state.series}
        typs='line'
        width={500}
        height={300}
        />
        {/* <h1>{keys}</h1> */}
        </div>
    );
  }
}

export default MyChart;