import React from "react";

type TypeProps = {
  name: string;
  placeholder: string;
};

export default function Input({ name, placeholder }: TypeProps) {
  return (
    <input
      className="form-input border-none rounded-md invert-[1]"
      type="text"
      name="title"
      placeholder="Title"
    />
  );
}
