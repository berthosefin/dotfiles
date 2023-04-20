import React from "react";

export default function Input({ name, placeholder }) {
  return (
    <input
      className="form-input border-none rounded-md invert-[1]"
      type="text"
      name="title"
      placeholder="Title"
    />
  );
}
