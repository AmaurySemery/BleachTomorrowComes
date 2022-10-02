public static void lireSite(String "https://www.before-tomorrow-comes.fr/memberlist") throws MalformedURLException, IOException
{
    String regex = "\\<label for=\"([^\\\"]*)\"\\>([^\\<]*)\\</strong\\>";
    
    Scanner sc = new Scanner(new URL(url).openStream());
    
    while (sc.hasNextLine())
    {
        String line = sc.nextLine();
        if (line.matches(regex))
        {
            Scanner sc2 = new Scanner(line);
            sc2.findInLine(regex);
            
            MatchResult result = sc2.match();
            System.out.printf("%s\t%s\n",result.group(1),result.group(2));
            sc2.close();
        }
    }
    sc.close();
}