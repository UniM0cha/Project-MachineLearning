import React,{useEffect} from "react";

import axios from 'axios';

import Header from "../components/Header";

const Axiostest = () => {

    useEffect(() => {
        axios.post('http://112.151.4.252:5000/product_list')
        .then((res) => console.log(res)).catch((err)=>{
            console.log(err)
        },[])
    })
    return(
        <div>
        <div><Header/></div>
        <h1>히히짜증나</h1>
        </div>

    )
}

export default Axiostest;