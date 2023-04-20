import React from "react";

type TypeProps = {
  name: string;
  placeholder?: string;
  type: "text" | "date" | "time";
};

export default function Input({ name, placeholder, type }: TypeProps) {
  return (
    <input
      className="border-none rounded-md"
      type={type}
      name={name}
      placeholder={placeholder}
    />
  );
}
