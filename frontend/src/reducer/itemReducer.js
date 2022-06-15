import{
    GET_ITEM,
    SEARCH_ITEMS,
    GET_ITEM_BY_CATEGORY,
    GET_ITEM_BY_ID,
    GET_PRODUCT_IMAGES,
    ADD_ITEM,
    UPDATE_ITEM,
    DELETE_ITEM,
    ITEMS_LOADING,
    EMPTY_ITEM
} from'../types/itemTypes'

constInitialState={
    items : [],
    productImgs : [],
    file : [],
    loading: true,
}

export const itemReduce = (state = InitialState, action)=>{
    const { type, payload } = action
    switch(type){
        case GET_ITEM:
            return{
                ...state,
                items : payload,
                loading: true
            }
        case SEARCH_ITEMS:
            return{
                ...state,
                items : payload,
                loading: true
            }
        case GET_ITEM_BY_CATEGORY:
            return{
                ...state,
                items : payload,
                loading: true
            }
        case GET_ITEM_BY_ID:
            return{
                ...state,
                items : payload,
                loading: true
            }
        case GET_PRODUCT_IMAGES:
            return{
                ...state,
                productImgs : payload,
                loading: true
            }
        case ADD_ITEM:
            return{
                ...state,
                loading: false,
            }
        case UPDATE_ITEM:
            return{
                ...state,
                loading: false,
            }
        case DELETE_ITEM:
            return{
                ...state,
                loading: false,
            }
        case ITEMS_LOADING:
            return{
                ...state,
                loading: true,
            }
        case EMPTY_ITEM:
            return{
                ...state,
                items : [],
                loading: true
            }
            default:
                return state;
        }
}