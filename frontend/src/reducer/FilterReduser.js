import{
    FILTER_PRICE,
    FILTER_RATING,
    FILTER_CONDITION,
    FILTER_PRICE_AND_RATING,
    FILTER_PRICE_AND_CONDITION,
    FILTER_ALL
} from'../types/filterTypes'

constInitialState={
    products : [],
    loading: true,
}

export const filterReduce = (state = InitialState, action)=>{
    const { type, payload } = action
    switch(type){
        case FILTER_PRICE:
            return{
                ...state,
                products: payload,
                loading:false
            }
        case FILTER_RATING:
            return{
                ...state,
                products: payload,
                loading:false
            }
        case FILTER_CONDITION:
           return{
                ...state,
                products: payload,
                loading:false
            }
        case FILTER_PRICE_AND_RATING:
            return{
                ...state,
                products: payload,
                loading:false
            }
        case FILTER_PRICE_AND_CONDITION:
            return{
                ...state,
                products: payload,
                loading:false
            }
        case FILTER_ALL:
            return{
                ...state,
                loadingCartItem: false,
            }
            default:
                return state;
        }
}