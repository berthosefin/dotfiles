import React from "react";

type TypeProps = {
  name: string;
  placeholder?: string;
  type: "text" | "date" | "time";
};

export default function Input({ name, placeholder, type }: TypeProps) {
  return (
    <input
      className="bg-[#2e3440] rounded text-[#fff555] px-3 py-1"
      type={type}
      name={name}
      placeholder={placeholder}
    />
  );
}
