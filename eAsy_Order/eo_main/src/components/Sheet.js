import React from "react";



const Sheets = () => {


    return (

        <div>
            <table id='customers'>
                <th>
                    아이템 번호
                </th>
                <th>
                    상품명
                </th>
                <th>
                    재고량
                </th>
                <th>
                    예측판매량
                </th>
                <th>
                    발주량
                </th>

                <tr>
                    <td>1</td>
                    <td>1번아이템</td>
                    <td>10</td>
                    <td>3</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>2번아이템</td>
                    <td>2</td>
                    <td>10</td>
                    <td>8</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>3번아이템</td>
                    <td>재고량</td>
                    <td>예측판매량</td>
                    <td>발주량</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>4번아이템</td>
                    <td>재고량</td>
                    <td>예측판매량</td>
                    <td>발주량</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>5번아이템</td>
                    <td>재고량</td>
                    <td>예측판매량</td>
                    <td>발주량</td>
                </tr>
            </table>
        </div>

    )
}

export default Sheets