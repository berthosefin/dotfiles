import Link from "next/link";
import React from "react";

export default function Header() {
  return (
    <div className="py-5 bg-[#2E3440] text-[#D8DEE9] text-bold text-2xl">
      <div>
        <Link href={"/"}>Tech List</Link>
      </div>
    </div>
  );
}
