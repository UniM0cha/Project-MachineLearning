import React from "react";




const Login = () => {

    return (
        <div className="body"
            style={{
                display: 'flex',
                justifyContent: 'center',
                
                alignItems: 'center',
                width: '100%',
                height: '100vh',
            }}
        >
            <div style={{
              
                verticalAign : 'middle',
    
            }}>
        
                <h1 className="fadeleft"> 쉽고 편리한 자동 주문 system</h1>
          
                <h1 className="faderight">Easy_Order</h1>
          
            <div>
            <form style={{ display: 'flex', flexDirection: 'column', width: '300px', verticalAlign: "middle" }} >
                <label className="font-white">Email</label>
                <input type="id" />
                <label className="font-white">Password</label>
                <input type="pw"  />
                <br />
                <button type="submit" className="button" >Login</button>
            </form>
            </div>
        </div>
        </div>
    );


}




export default Login;