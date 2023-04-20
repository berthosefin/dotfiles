import { createListenerMiddleware } from "@reduxjs/toolkit";
import { toggleChangeAction, updateAction } from "./reducer";

const listenerMiddleware = createListenerMiddleware();
