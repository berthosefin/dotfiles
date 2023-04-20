import React from "react";

export default function layout({ children: React.ReactNode }) {
  return (
    <>
      <h2>Group of Tech</h2>
      {children}
    </>
  );
}
