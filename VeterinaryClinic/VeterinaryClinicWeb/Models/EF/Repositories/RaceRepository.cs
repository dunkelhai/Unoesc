using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Models.EF.Repositories
{
    public class RaceRepository : RepositoryBase<Race>, IRaceRepository
    {
        public RaceRepository(BancoContext context) : base(context) { }

        protected override IQueryable<Race> DefaultQuery => 
            base.DefaultQuery.Include(r => r.Specie);
    }
}