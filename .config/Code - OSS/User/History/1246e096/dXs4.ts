import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  client: {
    toggleForm: false,
  },
};

export const ReducerSlice = createSlice({
  name: "next-crud",
  initialState,
  reducers: {
    toggleChangeAction: (state) => {
      state.client.toggleForm = !state.client.toggleForm;
    },
    updateAction: (state, action) => {
      state.client.formId;
    },
  },
});

export const { toggleChangeAction } = ReducerSlice.actions;

export default ReducerSlice.reducer;
