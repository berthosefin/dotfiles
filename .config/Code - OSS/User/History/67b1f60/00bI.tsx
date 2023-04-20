import Link from "next/link";
import React from "react";

export default function Header() {
  return (
    <div className="py-5 bg-[#D8DEE9]">
      <div>
        <Link href={"/"}>Tech List</Link>
      </div>
    </div>
  );
}
