"use client";
import { cva } from "class-variance-authority";
import React from "react";

interface Props {
  children: React.ReactNode;
}

const Navigator: React.FC<Props> = ({ children }) => {
  return (
    <main className="relative min-h-screen overflow-x-hidden flex w-full">
      <div>Sidebar</div>
      <div>Content</div>
    </main>
  );
};

export default Navigator;
