import React,{useState} from "react";

//haeder
import Header from '../components/Header';


// 
import SheetNonAuto from "../components/SheetNonAuto";


import axios from 'axios';


// 서버에 보낼 값
const BALJU_LIST = [
    { "product_id": 6, "order": 3 },
    { "product_id": 8, "order": 8 },
    { "product_id": 10, "order": 5 }
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
            {product_id: 6, order: 3},
            {product_id: 8, order: 8},
            {product_id: 10, order: 5},
           
        
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
       window.location.href = '/managena';
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