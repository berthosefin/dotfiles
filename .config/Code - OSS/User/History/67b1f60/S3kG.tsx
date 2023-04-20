import Link from "next/link";
import React from "react";

export default function Header() {
  return (
    <div className="py-5 bg-[#4C566A]">
      <div>
        <Link href={"/"}>Tech List</Link>
      </div>
    </div>
  );
}
