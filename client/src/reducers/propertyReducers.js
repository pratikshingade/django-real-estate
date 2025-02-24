import {createSlice} from "@reduxjs/toolkit";
import {PROPERTY_LIST_FAIL, PROPERTY_LIST_REQUEST, PROPERTY_LIST_SUCCESS} from "../actions/types.js";

const initialState = {
    properties: [],
};

const propertiesSlice = createSlice({
    name: "propertiesList",
    initialState,
    reducers: {
        setProperties: (state, action) => {
            switch (action.type) {
                case PROPERTY_LIST_REQUEST:
                    return {loading: true, initialState}

                case PROPERTY_LIST_SUCCESS:
                    return {loading: false, properties: action.payload.results}

                case PROPERTY_LIST_FAIL:
                    return {loading: false, error: action.payload}

                default:
                    return state
            }
            // state.properties = action.payload;
        },
    },
});

export const { setProperties } = propertiesSlice.actions;
export default propertiesSlice.reducer;  // ✅ Default export
