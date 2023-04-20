import React from "react";

type Props = {
  children: React.ReactNode;
};

export default function AppProvider({ children }: Props) {
  return { children };
}
