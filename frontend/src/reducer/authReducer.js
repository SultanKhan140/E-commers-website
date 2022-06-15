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

constInitialState={
    token: localStorage.getItem('token'),
    isAuthanticated: null,
    isLoading: null,
    user: null,
    msg: ""
}

export const authReduce = (state = InitialState, action)=>{
    const { type, payload } = action
    switch(type){
        case USER_LOADING:
            return{
                ...state,
                isLoading:true
            }
        case USER_LOADED:
            return{
                ...state,
                isLoading:false,
                isAuthanticated:true,
                user : payload
            }
        case AUTH_ERORR:
        case LOGIN_SUCCESS:
                localStorage.setItem('token',JSON.stringify(payload))
            return{
                ...state,
                isLoading:false,
                isAuthanticated:true,
                msg: "login Success"
            }
        case LOGIN_FAIL:
        case LOGOUT_SUCCESS:
                localStorage.removeItem('token')
            return{
                ...state,
                token: null,
                isAuthanticated: false,
                isLoading:false
            }
        case REGISTER_SUCCESS:
                localStorage.removeItem('token',JSON.stringify(payload))
            return{
                ...state,
                isLoading:false,
                isAuthanticated:true,
                msg: "Register Success"
            }
        case REGISTER_FAIL:
                localStorage.removeItem('token')
            return{
                ...state,
                token: null,
                isAuthanticated: false,
                isLoading:false
            }
            default:
                return state;
        }
}