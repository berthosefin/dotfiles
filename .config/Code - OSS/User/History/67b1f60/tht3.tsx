"use client";

import Link from "next/link";
import React from "react";
import { usePathname } from "next/navigation";

export default function Header() {
  const pathname = usePathname()?.split("/");
  const currentGroup = pathname ? pathname[2] ; null;
  const techId = pathname[3];
  return (
    <div className="py-5 bg-[#2E3440]">
      <div>
        <Link href={"/"}>
          <h1 className="text-[#D8DEE9] font-bold text-3xl text-center">
            TECH LIST
          </h1>
        </Link>
      </div>
      {pathname && currentGroup && (
        <Link href={techId ? `/techGroup/${currentGroup}` : "/techGroup"}>
          Back to {techId ? `${currentGroup}` : "Group of Tech"}
        </Link>
      )}
    </div>
  );
}
