import React from "react";

type TypeProps = {
  name: string;
  placeholder?: string;
  type: "text" | "date";
};

export default function Input({ name, placeholder, type }: TypeProps) {
  return (
    <input
      className="form-input border-none rounded-md invert-[1]"
      type={type}
      name={name}
      placeholder={placeholder}
    />
  );
}
