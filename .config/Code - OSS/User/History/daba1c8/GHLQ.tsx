type PageProps = {
  params: {
    searchTerm: string;
  };
};

export default async function SearchResults({
  params: { searchTerm },
}: PageProps) {
  const SearchResults = await Search(searchTerm);
  return <div>SearchResults</div>;
}
