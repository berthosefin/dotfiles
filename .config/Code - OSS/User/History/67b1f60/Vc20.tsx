import Link from "next/link";
import React from "react";

export default function Header() {
  return (
    <div className="py-5 bg-[#2E3440]">
      <div>
        <Link href={"/"}>
          <h1 className="text-[#D8DEE9] font-bold text-3xl text-center">
            Tech List
          </h1>
        </Link>
      </div>
    </div>
  );
}
