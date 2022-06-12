import React from 'react';
import { findAllInRenderedTree } from 'react-dom/test-utils';

// route
// import { useHistory } from "react-router";
import EoMain from './EoMain';

const Login = () => {
    const onLogin = () => {
        // const history = useHistory();
        let id = document.querySelector('#id');
        let pw = document.querySelector('#pw');

        if (id.value === '' || pw.value === '') {
            alert('id/pw가 입력이 되지 않았습니다.');
        } else if (id.value !== 'admin' || pw.value !== '1234') {
            alert('회원이 아닙니다.');
        } else {
            alert('어서오세요');
            window.location.href = '/main';
        }
    };

    return (
        <div
            className="body"
            style={{
                display: 'flex',
                justifyContent: 'center',

                alignItems: 'center',
                width: '100%',
                height: '100vh',
            }}
        >
            <div
                style={{
                    verticalAign: 'middle',
                }}
            >
                <h1 className="fadeleft"> 쉽고 편리한 자동 주문 system</h1>

                <h1 className="faderight">Easy_Order</h1>

                <div>
                    <div
                        style={{
                            display: 'flex',
                            flexDirection: 'column',
                            width: '300px',
                            verticalAlign: 'middle',
                        }}
                    >
                        <label className="font-white">ID</label>
                        <input type="id" id="id" />
                        <label className="font-white">Password</label>
                        <input type="password" id="pw" />
                        <br />
                        <button className="button" onClick={onLogin}>
                            Login
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Login;
