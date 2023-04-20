import Link from "next/link";
import { usePathname } from "next/navigation";

type TypeProps = {
  href: string;
  children: string;
};

export default function NavLink({ href, children }: TypeProps) {
  return <Link href={href}>{children}</Link>;
}
