import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    properties: [],
};

const propertiesSlice = createSlice({
    name: "propertiesList",
    initialState,
    reducers: {
        setProperties: (state, action) => {
            state.properties = action.payload;
        },
    },
});

export const { setProperties } = propertiesSlice.actions;
export default propertiesSlice.reducer;  // ✅ Default export
