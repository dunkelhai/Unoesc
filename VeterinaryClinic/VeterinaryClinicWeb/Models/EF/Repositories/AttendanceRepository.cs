using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Models.EF.Repositories
{
    public class AttendanceRepository : RepositoryBase<Attendance>, IAttendanceRepository
    {
        public AttendanceRepository(BancoContext context) : base(context) { }

        protected override IQueryable<Attendance> DefaultQuery =>
            base.DefaultQuery.Include(a => a.Animal).Include(v => v.Vet).Include(c => c.Clinic).Include(p => p.Procedures);
    }
}