"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

type TypeProps = {
  href: string;
  children: string;
};

export default function NavLink({ href, children }: TypeProps) {
  const path = usePathname();
  console.log(path);
  const active = href === path;

  return <Link href={href}>{children}</Link>;
}
