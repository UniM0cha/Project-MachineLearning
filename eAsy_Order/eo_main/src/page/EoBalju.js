import React,{useState} from "react";

//haeder
import Header from '../components/Header';


// 
import SheetNonAuto from "../components/SheetNonAuto";


import axios from 'axios';

const BALJU_LIST = [
    { "product_id": 1, "order": 3 },
    { "product_id": 2, "order": 19 },
    { "product_id": 3, "order": 4 }
];

const EoBalju = () => {

    const[checkList, setCheckList]  = useState([]);
    const onChecked = (cheked, item) => {
        if(cheked){
            setCheckList([...checkList, item]);
        }
    }

    const baljuGo = () => {
        // 발주 버튼 누르면
    
        let sendData = {
          stroe_id : 1,
    
          order: [
            {product_id: 1, order: 3},
            {product_id: 2, order: 19},
            {product_id: 3, order: 4},
            {product_id: 4, order: 4},
            {product_id: 5, order: 4}
          ]
        };
    
        const option = {
          method : "POST",
          url : "http://112.151.4.252:5000/order",
          data : sendData
        };
    
       axios(option).then(({data}) => {
        console.log(data);
       }).catch((error) => {
        console.log(error)
       })
       alert("주문 완료하였습니다")
       window.location.href = '/main';
      }
    

    return(
        <div>
        <div><Header/></div>
        <div className='mainParents'><SheetNonAuto/></div>
        <div className='buttonhi'><button onClick={baljuGo} className="buttonhi"  >발주 주문 넣기</button></div>
        </div>
    )
} 

export default EoBalju;