import{
    USER_LOADING,
    USER_LOADED,
    AUTH_ERORR,
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    LOGOUT_SUCCESS,
    REGISTER_SUCCESS,
    REGISTER_FAIL
} from'../types/authTypes'


import axios from "axios";
import { queryAllByAttribute } from '@testing-library/react';


export const loadUser = ()=>(dispatch)=>{
    dispatch({type : USER_LOADING });
    const config={
        Headers:{
            'Content-type' : 'application/json'
        }
    }

    axios.get('${process.env.SERVER_URL}api/user',config).then((res)=>{
        dispatch({
            type:USER_LOADED,
            payload: res.data
        })
    })
}

export const register = (data)=>async(dispatch)=>{
    dispatch({type : USER_LOADING });
    const config={
        Headers:{
            'Content-type' : 'application/json'
        }
    }

    await axios.post('${process.env.SERVER_URL}api/user',config).then((res)=>{
        await axios.post('${process.env.SERVER_URL}api/user',{'userId':res.data?.id,"quantity":0}.config).then((res)=>{
            dispatch({
                type:REGISTER_SUCCESS,
                payload: res.data
            })
        })
}).catch(err=>{
    dispatch({
        type: REGISTER_FAIL,
        msg: err.response.data
    })

    })
}

export const login = (email, password)=>async(dispatch)=>{
    dispatch({type : USER_LOADING });
    const config={
        Headers:{
            'Content-type' : 'application/json'
        }
    }

    await axios.post('${process.env.SERVER_URL}api/login/${email}/',config).then((res)=>{
        if(res.data.length === 0){
            alart("email not registered");
            dispatch({
                type: LOGIN_FAIL,
                msg: "email not registered"
            })
        }else{
            let emailinDB = res.data[0]?.email;
            let passwordinDB = res.data[0]?.password;

            if(emailinDB===email && passwordinDB===password){
                dispatch({
                    type: LOGIN_SUCCESS,
                    payload: res.data[0] 
                })
            }else{
                alart("wrong password")
                dispatch({
                    type:LOGIN_FAIL,
                    msg: "wrong password"
                })
            }
        }
}).catch(err=>{
    dispatch({
        type: REGISTER_FAIL,
        msg: err.response.data
    })
})
}

export const logout = ()=>async(dispatch)=>{
    dispatch({
        type:LOGOUT_SUCCESS,
        msg: err.response.data
    })
}