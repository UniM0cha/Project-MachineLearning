import React,{useState} from "react";

//haeder
import Header from '../components/Header';

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

    return(
        <div>
        <div><Header/></div>
      
        </div>
    )
} 

export default EoBalju;