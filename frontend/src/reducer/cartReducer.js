import{
    GET_CART,
    ADD_TO_CART,
    DELETE_FROM_CART,
    CART_LOADING,
    GET_ITEMS_CART,
    ADD_ITEMS_TO_CART,
    DELETE_ITEMS_TO_CART,
    CART_ITEM_LOADING
} from'../types/cartTypes'

constInitialState={
    cart : [],
    cartItem: [],
    loadingCart : false,
    loadingCartItem : false,
}

export const cartReduce = (state = InitialState, action)=>{
    const { type, payload } = action
    switch(type){
        case GET_CART:
            return{
                ...state,
                cart: payload,
                loadindCart:false
            }
        case ADD_TO_CART:
            return{
                ...state,
                cart: payload,
                loadingCart:false
            }
        case DELETE_FROM_CART:
            return{
                ...state,
                cart: payload,
                loadingCart:false
            }
        case CART_LOADING:
            return{
                ...state,
                cart: payload,
                loadingCart:true
            }
            case GET_ITEMS_CART:
                return{
                    ...state,
                    cartItem: payload,
                    loadingCartItem: false
                }
            case ADD_ITEMS_TO_CART:
            return{
                ...state,
                loadingCartItem: false,
            }
            case DELETE_ITEMS_TO_CART:
            return{
                ...state,
                loadingCartItem: false,
            }
            case CART_ITEM_LOADING:
                localStorage.removeItem('token')
             return{
                ...state,
                loadingCartItem: true,
            }
            default:
                return state;
        }
}