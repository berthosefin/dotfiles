import React from "react";

interface Props {
  children: React.ReactNode;
}

const Navigator: React.FC<Props> = ({ children }) => {
  return (
    <div className="relative min-h-screen overflow-x-hidden flex w-full">
      Navigator
    </div>
  );
};

export default Navigator;
