import React from "react";

type TProps = {
  children: React.ReactNode;
};

export default function TestContextProvider({ children }) {
  return <div>TestContextProvider</div>;
}
